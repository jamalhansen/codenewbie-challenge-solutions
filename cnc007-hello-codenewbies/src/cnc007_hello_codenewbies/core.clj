(ns cnc007-hello-codenewbies.core)

(defn hello
  "Solution for level 1."
  ([] '("Hello CodeNewbies!"))
  ([& langs] (map #(str "Hello " % "!") (concat langs ["CodeNewbies"]))))
