(ns fortissimo.core)

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))

(defn zip [v1 v2]
  (map vector 'v1 'v2))

(defn BcInst [opcode ret]
  {:opcode opcode, :ret ret})

(defn BcInstBase [opcode ret reg1 reg2 reg3]
  {:opcode opcode, :ret ret, :reg1 reg1, :reg2 reg2, :reg3 reg3})

(defn BcInstSpec [opcode args body reg1]
  {:opcode opcode, :args args, :body body, :reg1 reg1})

(def cnt 0)

(defn bytecode [e]
  (letfn newTemp []
    (def cnt (+ cnt 1))
    (str "$" cnt))
  (letfn bc [e t]
    (let t1 (newTemp))
    (let t2 (newTemp))
    (let t3 (newTemp))
    (let retn 0)))


(defn State [stmts env pc callstack]
  ; remember that callstack is by default a list
  {:stmts stmts, :env env, :pc pc, :callstack callstack}
  )

(gen-and-load-class 'user.ProgramEndException :extends Exception)

(defn ProgramEnd [exit_value]
  ; Need to store info in exception
  (throw (new user.Exception str(exit_value))))

(defn Fun [argList body]
  {:argList argList, :body body})

(defn FunVal [fun env]
  {:fun fun, :env env})

(def globEnv {:__up__ nil})

(defn Exec [stmts]
  (let env {:__up__ nil})
  (Resume (State stmts env)))

(defn ExecFun [closure args]
  (let env (zipmap ((closure :fun) :argList) args))
  (let env (assoc env :__up__ (closure :env)))
  (nth (Resume (State(((closure :fun) :body), env))) 1))

(defn ExecFunByName [stmts funName args]
  (let env {:__up__ nil})
  (Resume (State stmts env))
  (ExecFun((env funName) args))

(defn ExecGlobal [ast]
  (let bc (bytecode (desugar ast)))
  (tcall_opt bc)
  (Resume (State bc globEnv)))

(defn Resume [state]
  (letfn lookup [name]
    (try (env name)
      (do (cond (= (env :__up__) nil)
                (throw (Exception. (str "Cannot find " name)))
                (lookup name (env :__up__))))))
  (letfn update [name val env]
    (try (cond (contains? env name) 
               (let env (assoc env name val))
               (update name val (env :__up__)))
      (throw (Exception. (str "Cannot overwrite variable, cannot find " name)))))

  (letfn define [name val]
    (let state (assoc state :env (assoc (state :env) name val))))

  (letfn addScope [parentEnv]
    {:__up__ parentEnv})

  (letfn execCall [state]
    (let lhsVar (inst :ret))
    (let func (lookup (inst :reg1)))
    (cond (and (contains? func :fun) (contains? func :env))
      (throw (Exception. "Trying to call non-lambda")))
    (let fbody ((func :fun) :body))
    (let fargs ((func :fun) :argList))
    (let fenv (func :env))
    (let aargs (for [a (inst :args)] (lookup a))); Finish list comp
    (let state (assoc state :callstack (conj (state :callstack) (list (state :stmts) (state :pc) (state :env) lhsVar))))

    (let state (assoc state :env (addScope fenv)))
    (let state (assoc state :env (merge (state :env) (zipmap fargs aargs))))

    (let state (assoc state :stmts fbody))
    (let state (assoc state :pc 0))
  )

  (letfn execReturn [state]
    (cond (= (count (state :callstack)) 0) (ProgramEnd (list (lookup (inst :ret)) nil true)))
    (let retVal (lookup (inst :ret))))

  (let actions {})

  (while true (do 
                (let inst ((state :stmts) (state :pc)))
                (let state (assoc state :pc (+ (state :pc) 1)))
                (try (catch user.ProgramEndException e (e.exit_value))))) 
)

(defn desugar [stmts]
  (letfn desugarExp [e]
    (let retnDesugarExp 0)
  )
  (letfn desugarStatments [stmtss]
    (let dStmts (list))
  )
  (desugarStatements stmts)
)
