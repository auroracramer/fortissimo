; All instruments have the interface (<instr> <abs-note> <duration>)
(ns fortissimo.instruments
  (:use [overtone.live]
        [overtone.inst.synth]
        [overtone.inst.sampled-piano]))

(defn getDuration [duration tempo]
  (/ (* duration 60.0) tempo))

; User defined instrument should be wrapped in this function
(defn userInstrument [name_, instr]
  (def instrs (assoc instrs name_ instr)))

(definst saw-wave [freq 440 attack 0.01 sustain 0.4 release 0.1 vol 0.5] 
    (* (env-gen (lin-env attack sustain release) 1 1 0 1 FREE)
       (saw freq)
        vol))

(defn note->hz [music-note]
  (midi->hz (note music-note)))

(def instrs {
  "Piano" (fn [pitch duration tempo]  (sampled-piano :level 0.5 :note (note pitch) :sustain (getDuration duration tempo))),
  "SawWave" (fn [pitch duration tempo] (saw-wave :freq (note->hz pitch) :sustain (getDuration duration tempo)))
  "Synth" (fn [pitch duration tempo] (tb303 :note (note pitch) :release (getDuration duration tempo) :sustain 50))
  "Guitar" (fn [pitch duration tempo] (ks1 :note (note pitch) :dur (getDuration duration tempo)))
  "Overpad" (fn [pitch duration tempo] (overpad :note (note pitch) :release (getDuration duration tempo)))
  "Ping" (fn [pitch duration tempo] (ping :note (note pitch) :decay (getDuration duration tempo)))
  "Bass" (fn [pitch duration tempo] (bass :freq (note->hz pitch) :t (getDuration duration tempo)))
  })
