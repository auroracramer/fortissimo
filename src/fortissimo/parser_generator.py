import grammar, grammar_parser, re, sys, types, util
from util import Ambiguous
from collections import defaultdict
import string
import pprint

##-----------------------------------------------------------------------------
## Module interface
##

def makeRecognizer (gram, type='earley'):
    '''Construct and return a "recognizer" of GRAM.

    A recognizer is an object with a method recognize(inp), returning
    True if INP is a valid string in GRAM, and False otherwise.
    '''
    class Recognizer:
        def __init__ (self, parser):
            self.parser = parser

        def dump (self, f=sys.stdout):
            self.parser.dump (f)
        
        def recognize (self, inp):
            if self.parser.recognize(inp):
                return True
            return False

    return Recognizer (makeParser (gram, type))


def makeParser (gram, type='earley'):
    '''Construct and return a parser of GRAM.

    A parser is an object with a method parse(inp), returning the AST
    constructed from the parse tree of INP by the semantic actions in GRAM.
    '''
    if type == 'earley':
        return EarleyParser (gram)
    else:
        raise TypeError, 'Unknown parser type specified'

##-----------------------------------------------------------------------------
## Parse Tree code removed for now.  You will get it in PA6


# def wrapper(funct,arg):
#         return funct(*arg)

class ParseTree:
    def __init__ (self):
        self.rootEdge = None
        self.LHS = None
        self.RHS = None
        self.val = None
        self.op = None
        self.parent = None
        self.edges = None

    def createParseTree(self, root, Children, edges):
        self.edges = edges
        self.rootEdge = root
        (i,j,prod,pos) = root
        argList = [prod.LHS]
        listOfChildren = []
        for element in Children:
            if type(element) != tuple:
                listOfChildren.append(element)
            else:
                (csrc,cdst,cprod,cpos) = element
                listOfChildren.append((csrc,cdst,cprod.LHS,cprod.RHS,cpos))
                
        if len(Children) == 0:
            self.LHS = self.createChild(None,root)
            if prod.actions[1] != None:
                function = prod.actions[1]
                self.val = function(prod.LHS,self.LHS)
            else:
                function = lambda LHS, N1: N1.val
                self.val = function(prod.LHS,self.LHS)

        else:
            for x in xrange(0,len(Children)):
                argList.append(self.createChild(Children[x],root))
            if prod.actions[len(prod.RHS)] == None:
                function = lambda LHS, N1: N1.val
                self.val = function(prod.LHS,argList[1])
            else:
                function = prod.actions[len(prod.RHS)]
                self.val = function(*argList)

    def createChild(self, root, parent):
        Child = ParseTree()
        Child.parent = parent
        if (type(root) == tuple) and (len(root) == 4):
            (src,dst,prod,pos) = root
            edgeDst = self.edges(dst,0)
            Children = edgeDst[2][(src,dst,prod,pos)]
            Child.createParseTree(root, Children, self.edges)
            return Child
        else:
            Child.val = root
            return Child

##-----------------------------------------------------------------------------
## Earley Parser
##
class EarleyParser:
    '''A parser implementing the Earley algorithm.'''

    def __init__ (self, gram):
        '''Create a new Earley parser.'''
        self.grammar = gram
        self.terminals, self.invRenamedTerminals = EarleyParser.preprocess (gram)

    def parse (self, inp):

        def EarlyParse(grammar, inp):    
            graph = defaultdict(lambda: ([],set(),{}))
            complete = 0
            inProgress = 1
            ambiguousDict = {}
            def edgesIncomingTo(dst,status):
                key = (dst,status)
                return graph[key]
            
            def disambiguate(p1,p2,p1Tree,p2Tree):
                if p1.opPrec != None and p2.opPrec != None:
                    if p1.opPrec == p2.opPrec:
                        if p1.opAssoc[0] == 'left':
                            (src1,dst1,prod1,pos1) = p1Tree[0]
                            (src2,dst2,prod2,pos2) = p2Tree[0]
                            if (dst1 - src1) < (dst2-src2):
                                return (p2,p2Tree)
                            else:
                                return (p1,p1Tree)
                        else:
                            (src1,dst1,prod1,pos1) = p1Tree[2]
                            (src2,dst2,prod2,pos2) = p2Tree[2]
                            if (dst1 - src1) < (dst2-src2):
                                return (p2,p2Tree)
                            else:
                                return (p1,p1Tree)
                    else:
                        if p1.opPrec < p2.opPrec:
                            return (p1,p1Tree)
                        else:
                            return (p2,p2Tree)
                elif p1.prec >-1 and p2.prec > -1:
                    if p1.prec > p2.prec:
                        return (p1,p1Tree)
                    elif p1.prec < p2.prec:
                        return (p2,p2Tree)
                    elif p1.prec == p2.prec:
                        resolve[0] = False
                        return (p1,p1Tree)
                else:
                    resolve[0] = False
                    return (p1,p1Tree)

            def addEdge(e):
                (src,dst,prod,pos,treeChild) = e
                e2 = (src,dst,prod,pos)
                RHS = prod.RHS
                status = complete if len(RHS) == pos else inProgress
                (edgeList,edgeSet,edgeChild) = edgesIncomingTo(dst,status)
                if e2 not in edgeSet:
                    if status == complete:
                        newProd = prod
                        if (src,dst,prod.LHS) not in ambiguousDict:
                            ambiguousDict[(src,dst,prod.LHS)] = prod
                        elif ambiguousDict[(src,dst,prod.LHS)] != prod:
                            amb[0] = True
                            oldProd = ambiguousDict[(src,dst,prod.LHS)]
                            if e2 in edgeChild:
                                oldTree = edgeChild[e2]
                            else:
                                oldTree = edgeChild[(src,dst,oldProd,len(oldProd.RHS))]
                            (newProd,treeChild) = disambiguate(oldProd,prod,oldTree,treeChild)
                            
                            if (src,dst, oldProd, len(oldProd.RHS)) in edgeList:
                                edgeList.remove((src,dst, oldProd, len(oldProd.RHS)))
                                del edgeChild[(src,dst, oldProd, len(oldProd.RHS))]
                            e3 = (src,dst,newProd,len(newProd.RHS))
                            edgeChild[e3] = treeChild
                            edgeList.append(e3)
                            edgeSet.add(e3)
                            ambiguousDict[(src,dst,prod.LHS)] = newProd
                            return False
                    edgeChild[e2] = treeChild
                    edgeList.append(e2)
                    edgeSet.add(e2)
                    return True
                else:
                    if status == complete:
                        oldProd = ambiguousDict[(src,dst,prod.LHS)]
                        if e2 in edgeChild:
                            oldTree = edgeChild[e2]
                        else:
                            oldTree = edgeChild[(src,dst,oldProd,len(oldProd.RHS))]
                        if oldTree != treeChild:
                            oldProd = ambiguousDict[(src,dst,prod.LHS)]
                            (newProd,newChild) = disambiguate(oldProd,prod,oldTree,treeChild)
                            edgeChild[e2] = newChild
                    return False
            
            sbol = grammar.startSymbol
            for P in grammar[sbol].productions:
                addEdge((0,0,P,0,[]))
            for j in xrange(0,len(inp)+1):
                if j > 0:
                    for (i,_j,prod,pos) in edgesIncomingTo(j-1,inProgress)[0]:
                        assert _j==j-1
                        if pos<len(prod.RHS) and prod.RHS[pos] == inp[j-1][0]:
                            treeChild = edgesIncomingTo(j-1,inProgress)[2][(i,_j,prod,pos)]
                            listTreeChild = treeChild
                            listTreeChild.append(inp[j-1][1])
                            addEdge((i,j,prod,pos+1,listTreeChild))
                edgeWasInserted = True
                while edgeWasInserted:
                    edgeWasInserted = False
                    for (i,_j,prod,pos) in edgesIncomingTo(j,complete)[0]:
                        assert _j == j and pos == len(prod.RHS)
                        for (k,_i,prod2,pos2) in edgesIncomingTo(i,inProgress)[0]:
                            assert _i == i and pos2 < len(prod2.RHS)
                            if prod2.RHS[pos2] == prod.LHS:
                                listTreeChild = []
                                treeChild2 = edgesIncomingTo(i,inProgress)[2][(k,_i,prod2,pos2)]
                                listTreeChild.extend(treeChild2)
                                listTreeChild.extend([(i,_j,prod,pos)])
                                newTreeChild = listTreeChild
                                edgeWasInserted = addEdge((k,j,prod2,pos2+1,newTreeChild)) or edgeWasInserted
                    for (i,_j,prod,pos) in edgesIncomingTo(j,inProgress)[0]:
                        assert _j == j and pos < len(prod.RHS)
                        if prod.RHS[pos] in string.ascii_uppercase or (len(prod.RHS[pos])>1 and prod.RHS[pos][0] in string.ascii_uppercase):
                          M = prod.RHS[pos]
                          for prod in grammar[M].productions:
                                edgeWasInserted = addEdge((j,j,prod,0,[])) or edgeWasInserted
                                
            for prod in grammar[sbol].productions:
                if (0,len(inp),prod,len(prod.RHS)) in edgesIncomingTo(len(inp),complete)[1]:
                    innerChild = edgesIncomingTo(len(inp),complete)[2][(0,len(inp),prod,len(prod.RHS))]
                    (isrc,idst,iprod,ipos) = innerChild[0]
                    root = (0,len(inp),prod,len(prod.RHS))
                    children = edgesIncomingTo(len(inp),complete)[2][(0,len(inp),prod,len(prod.RHS))]
                    edges = edgesIncomingTo
                    Tree = ParseTree()
                    Tree.createParseTree(root, children, edges)
                    parseTree[0]=Tree.val
                    return True
            return False
            
        try:
            tokens = self.tokenize (inp)
            TOKEN = 0; LEXEME = 1
        except Exception, pos:
            util.error ('Lexical error.  Cannot tokenize "at pos %s. Context: %s"'% (pos, inp[pos[0]:pos[0]+24]))
            return False
        amb = [False]
        resolve = [True]
        parseTree =[None]
        ParseOK = EarlyParse(self.grammar, tokens)
        if amb[0] == False and ParseOK :
            return parseTree[0]
        elif ParseOK and amb[0] == True and resolve[0] == True:
            return parseTree[0]
        elif not ParseOK and amb[0] == False:
            sys.stdout.write("Error")
            sys.exit(1)
        else:
            return parseTree[0]
            
    def tokenize (self, inp):
        '''Return the tokenized version of INP, a sequence of
        (token, lexeme) pairs.
        '''
        tokens = []
        pos = 0

        while True:
            matchLHS = 0
            matchText = None
            matchEnd = -1

            for regex, lhs in self.terminals:
                match = regex.match (inp, pos)
                if match and match.end () > matchEnd:
                    matchLHS = lhs
                    matchText = match.group ()
                    matchEnd = match.end ()

            if pos == len (inp):
                if matchLHS:  tokens.append ((matchLHS, matchText))
                break
            elif pos == matchEnd:       # 0-length match
                raise Exception, pos
            elif matchLHS is None:      # 'Ignore' tokens
                pass
            elif matchLHS:              # Valid token
                tokens.append ((matchLHS, matchText))
            else:                       # no match
                raise Exception, pos

            pos = matchEnd

        return tokens


    def dump (self, f=sys.stdout):
        '''Print a representation of the grammar to f.'''

        self.grammar.dump()

        for regex, lhs in self.terminals:
            if lhs is None:  lhs = '(ignore)'
            print lhs, '->', regex.pattern


    ##---  STATIC  ------------------------------------------------------------

    TERM_PFX = '*'     # prefix of nonterminals replacing terminals
    NONTERM_PFX = '@'  # prefix of nonterminals replacing RHSs with > 2 symbols

    @staticmethod
    def preprocess (gram):
        '''Returns the tuple:
        
        (
          [ (regex, lhs) ],             # pattern/token list
        )

        WARNING: modifies GRAM argument.
        '''

        REGEX = re.compile ('')
        
        terminals = []
        renamedTerminals = {}
        epsilons = []

        # Import all the grammar's modules into a new global object
        try:
            glob = util.doImports (gram.imports)
        except Exception, e:
            util.error ('problem importing %s: %s' % (gram.imports, str(e)))
            sys.exit(1)
        
        # Add 'ignore' patterns to the terminals list
        for regex in gram.ignores:
            terminals.append ((regex, None))

        # Add 'optional' patterns to the terminals list
        for sym, regex in gram.optionals:
            terminals.append ((regex, sym))

        # Build a lookup table for operator associavitiy/precedences
        operators = {}
        for op, prec, assoc in gram.getAssocDecls ():
            operators [op.pattern] = (prec, assoc)

        # First pass -- pull out epsilon productions, add terminal rules
        # and take care of semantic actions
        ruleNum = 0                     # newly-created rules
        for rule in gram.rules:
            lhs = rule.lhs
            for production in rule.productions:
                actions = production.actions
                rhs = list(production.RHS)

                # Create the S-action, if specified
                if actions[len (rhs)]:
                    actions[len (rhs)] = EarleyParser.makeSemantFunc (
                        actions[len (rhs)], len (rhs), glob)

                # Pull out epsilons and terminals
                for i, sym in enumerate (rhs):
                    if sym == grammar.Grammar.EPSILON:
                        # Epsilon
                        # 
                        # CYK: info = (None, None, None, production)
                        # CYK: epsilons.append ((lhs, info))
                        assert len (rhs) == 1
                        rhs = [] # in Earley, we model empsilon as an empty rhs
                        production.RHS = []

                    elif type (sym) == type (REGEX):
                        # Terminal symbol
                        if sym.pattern in renamedTerminals:
                            # Terminal was already factored out
                            termSym = renamedTerminals[sym.pattern]
                        else:
                            # Add *N -> sym rule, replace old symbol
                            termSym = '%s%d'% (EarleyParser.TERM_PFX, ruleNum)
                            ruleNum += 1
                            renamedTerminals[sym.pattern] = termSym
                            terminals.append ((sym, termSym))

                        if sym.pattern in operators:
                            # This pattern has a global assoc/prec declaration
                            # (which might be overridden later)
                            prec, assoc = operators[sym.pattern]
                            production.opPrec = prec
                            production.opAssoc = assoc
                        rhs[i] = termSym

                    if actions[i]:
                        # I-action for this symbol
                        actions[i] = EarleyParser.makeSemantFunc (
                            actions[i], len (rhs), glob)

                production.RHS = tuple(rhs)

        # Second pass -- build the symbol mapping and collect parsing info
        ruleNum = 0
        for rule in gram.rules:
            for production in rule.productions:
                lhs = rule.lhs
                rhs = production.RHS

                if len (rhs) == 1 and rhs[0] == grammar.Grammar.EPSILON:
                    # Epsilon production, skip it
                    continue

                # Collect precedence/associativity info
                if production.assoc != None:
                    # This production had a %prec declaration
                    opPrec, assoc = operators[production.assoc.pattern]
                elif production.opPrec != None:
                    # This production had a terminal symbol with an assoc/prec
                    # declaration
                    opPrec = production.opPrec
                    assoc = production.opAssoc
                else:
                    # No declarations ==> undefined prec, assoc
                    opPrec, assoc = None, None

                # Collect dprec info
                if production.prec != -1:
                    # Production had a %dprec declaration
                    dprec = production.prec
                else:
                    # No declaration ==> undefined dprec
                    dprec = None

                # Information about this production to be used during parsing
                production.info = (opPrec, assoc, dprec, production)
        
        return terminals, dict([(new,orig) for (orig,new) in renamedTerminals.iteritems()])


    @staticmethod
    def makeSemantFunc (code, numArgs, globalObject):
        args = ['n0']
        for i in xrange (numArgs):
            args.append ('n%d'% (i+1))
        try:
            return util.createFunction (util.uniqueIdentifier (),
                                        args, code, globalObject)
        except Exception, e:
            print e.msg
            util.error ("""couldn't create semantic function: """ + str(e))
            sys.exit(1)

    @staticmethod
    def __isTermSymbol (sym):
        '''Return TRUE iff SYM is a 'virtual' nonterminal for a
        terminal symbol, created during grammar normalization.
        '''
        return sym[0] == EarleyParser.TERM_PFX


    @staticmethod
    def dumpEdges (edges):
        '''Print a representation of the edge set EDGES to stdout.'''
        for sym, frm, to in edges:
            print '(%d)--%s--(%d)'% (frm, sym, to)


    @staticmethod
    def dumpTree (tree, edges, level=0):
        '''Print a representation of the parse tree TREE to stdout.'''
        sym, frm, to = tree[0:3]
        if len (tree) > 3:
            children = tree[3]
        else:
            children = edges[(sym, frm, to)][3]
        if (isinstance (children, types.StringType) or
            children is grammar.Grammar.EPSILON):
            print '%s%s "%s")'% ('-'*level*2, sym, children)
        else:
            print '%s%s %d-%d'% ('-'*level*2, sym, frm, to)
            for child in children:
                EarleyParser.dumpTree (child, edges, level + 1)

# For instrumentation 
def incr(id):
    pass 

if __name__ == '__main__':
    pass
