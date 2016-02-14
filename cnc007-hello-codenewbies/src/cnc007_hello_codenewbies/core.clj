(ns cnc007-hello-codenewbies.core
  (:gen-class))

(defn hello
  "Solution for all levels."
  [langs]
  (map #(str "Hello " % "!")
       (concat langs ["CodeNewbies"])))

(defn -main [& args]
  (apply println (hello args)))
