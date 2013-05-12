; All instruments have the interface (<instr> <abs-note> <duration>)
(ns fortissimo.instruments
  (:use overtone.live))

(use 'overtone.inst.sampled-piano)

(defn getDuration [duration tempo]
  (/ (* duration 60.0) tempo))

(definst saw-wave [freq 440 attack 0.01 sustain 0.4 release 0.1 vol 0.4] 
    (* (env-gen (lin-env attack sustain release) 1 1 0 1 FREE)
       (saw freq)
        vol))

(defn note->hz [music-note]
  (midi->hz (note music-note)))

(def instrs {
  "piano" (fn [pitch duration tempo]  (sampled-piano :note (note pitch) :sustain (getDuration duration tempo))),
  "saw-wave" (fn [pitch duration tempo] (saw-wave :freq (note->hz pitch) :sustain (getDuration duration tempo)))
  })
