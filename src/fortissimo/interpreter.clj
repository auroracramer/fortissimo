; Our beautiful Fortissimo interpreter
; <3 The Champions of Soda

; Returns a closure that has a body, argument list, and parent environment
(defn Closure [body args env]
  {:body body, :args args, :outer_env env})

; Util function for membership testing vectors
(defn in? [seq elm]
  (some #(= elm %) seq))

; Executes the simplified AST
(defn Exec [smts]
  ; Raises errors and exit
  (letfn raiseError []
    (print "Error!")
    (System/exit 0))

  ; Constructs a new environment with a parent environment, and includes
  ; default variables for the scale (C-maj scale), octave (4), and
  ; and instrument (piano). Also makes the field for the notes.
  (letfn newEnv [parent]
    {:_notes {}, :__up__ parent})

  ; Evaluate an expression in the context of an environment
  (letfn evalExp [e env]
    ; Lookup a name in the environment, or its parents and return it
    (letfn lookup [name env]
      (cond
        (empty? env) (raiseError) ; The enviroment shouldn't be empty
        (contains? env name) (env name) ; Return the name's binding if found
        :else (lookup name (env :__up__)))) ; Look in the parent otherwise
    (cond
      (= (first e) :phrase) (Closure (last e) (second e) env) ; Phrase lambda, return a closure
      :else (throw (Exception. "Illegal or Unimplemented AST node: "))))
  ; Evaluate a statement in the context of an environment
  (letfn evalStmt [stmts env]
    ; Update the environment and return it
    (letfn update [name env val]
      (cond
        (empty? env) (raiseError) ; The environment shouldn't be empty
        (contains? env name) (assoc env name val) ; If found, update the binding and return the env
        :else (assoc env :__up__ (update name (env :__up__) val)))) ; Otherwise, update in the parent, and reassign the changed parent in this env
    ; Evaluate each statement
    (doseq [s stmts]
      (let env (cond ; updates the environment after every pass
        (= (first s) :asgn) (update (second s) env (last s)) ; asgn - Binds a symbol to a new value
        (= (first s) :notes) (update :_notes env (addNotes (second s) env)) ; notes - adds notes to the note queue
        (= (first s) :play) (playPhrase (second s) (last s)) ; play - appends the notelist of the phrase to the queue of the current env
      )))
    env) ; return the environment
  ; Adds notes to the note queue and returns it back
  (letfn addNotes [newNotes env]
    ; TODO add error handling for erroneous notes
    
    ; Returns the scale number, accounting for a number above or below the
    ; length of the scale.
    (letfn noteMod [n scale]
      (let scaleLen (count scale))
      (cond ; Shouldn't be zero
        (< n 0) (cond ; If negative
          (= (mod (+ 1 n) scaleLen) 0) scaleLen 
          :else (mod (+ 1 n) scaleLen))
        (= (mod n scaleLen) 0) scaleLen ; Instead of being zero, the scale #s divisible
                                        ; by the scale length should be the scale length
        :else (mod n scaleLen)
        ))

    ; Returns the octave number of a note, given the notes position in the scale and the
    ; local scale
    (letfn octMod [n oct scale]
      ; The specified scale technically just sets the octave of the scale's first note
      (let note (noteMod n scale))
      (let scaleLen (count scale))
      ; Gets the letter of the note, as a string
      (letfn getBaseNote [note]
        (subs (str note) 1 2))
      ; Returns if a note in a scale is before C (when the octave increments)
      (letfn beforeC? [curr root]
        ; Check to see if the note is in the subvector of notes between the root
        ; and C
        (let letters ["C" "D" "E" "F" "G" "A" "B"])
        (in? (subvec letters (.indexOf letters root)) curr))
      ; Turns the number of scale steps above root into octaves above root, and adds it to
      ; any increment in octave from being C or above, and returns it
      (+ (cond 
           (< n 0) (- (int (/ (+ 1 n) scaleLen)) 1)
           :else (int (/ (- n 1) scaleLen)))
        (cond (beforeC? (getBaseNote note) (getBaseNote (first scale))) 0 :else 1))
      )
    
    ; Returns a note's duration given the note type, tempo, and meter
    (letfn noteDuration [duration tempo meter]
      )
    
    ; Get the note queue for the current instrument
    (let notes ((env :_notes) (env :_currInstr)))
    ; Add each note to the instrument's note queue
    (doseq [note newNotes]
      (cond
       ; If a scale note, find the absolute note by looking up the scale and octave
       (= (first note) :scale-note) (let notes (conj notes [(keyword (str (name ((env :_scale) (- (noteMod (second note) 1) (env :_scale)))) (octMod (second note) (env :_octave) (env :_scale)))) (env :_duration)]))
        )))
  ; Appends the notelist of the phrase to this phrase to the queue of the current environment
  ; At the end of the program, the queue is evaluated and played
  (letfn playPhrase [closure args]
    ; Add the argument bindings into the closures enviroment
    (doseq [i (range (count args))]
      (let new_env (assoc (newEnv (closure :outer_env)) (nth (closure :args) i) (nth args i))))
    ; Evaluate the body of the phrase
    (evalStmt (closure :body) new_env))
  ; Start executing the statements in the global environment
  (evalStmt stmts {:_scale [:C :D :E :F :G :A :B], :_octave 4, :_currInstr piano, :_duration :q, :_tempo 120, :_meter (/ 4 4), :_notes {}, :__up__ nil}))

; Desugars the AST into a simplified AST
(defn Desugar [ast]
  ; Desugars an expression
  (letfn desugarExp [e]
    (cond
      ;(= (first e) :<ASTNODE>) (comment asdfsdf )
      :else e))
  ; Desugar the statements
  (letfn desugarStmts [stmts]
    (let dStmts [])
    ; Desugar each statement
    (doseq [s stmts]
      (let dStmts (cond
      (= (first e) :playing) (conj dStmts [:asgn :_currInstr (second e)]) ; Desugar playing into reassigning the current instrument
      (= (first e) :phrase-def) (conj dStmts [:asgn (second e) [:phrase (nth e 2) (last e)]]) ; Desugar the phrase definition into assigning to a lambda
      :else (conj dStmts s))))) ; Otherwise, just pass through things that don't need to be desugared
  ; Desugar the AST
  (desugarStmts ast))

(defn Run [ast]
  (Exec (Desugar ast)))
