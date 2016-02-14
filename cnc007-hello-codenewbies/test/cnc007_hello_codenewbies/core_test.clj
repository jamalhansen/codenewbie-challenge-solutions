(ns cnc007-hello-codenewbies.core-test
  (:require [clojure.test :refer :all]
            [cnc007-hello-codenewbies.core :refer :all]))

(deftest lvl-one
  (testing "Level 1"
    (is (=  '("Hello CodeNewbies!") )(hello))))

(deftest lvl-two
  (testing "Level 2"
    (is (=  '("Hello Clojure!"
            "Hello CodeNewbies!") (hello "Clojure")))))

(deftest lvl-three
  (testing "Level 3"
    (is (=  '("Hello Clojure!"
            "Hello Python!"
            "Hello Javascript!"
            "Hello CodeNewbies!") (hello "Clojure" "Python" "Javascript")))))

