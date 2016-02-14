(ns cnc007-hello-codenewbies.core)

(defn hello
  "Solution for all levels."
  ([] '("Hello CodeNewbies!"))
  ([& langs] (map #(str "Hello " % "!") (concat langs ["CodeNewbies"]))))
