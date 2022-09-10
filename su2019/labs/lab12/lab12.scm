(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
            ( (y (repeatedly-cube (- n 1) x)) )
            (* y y y)))
)


; https://inst.eecs.berkeley.edu/~cs61a/su19/articles/scheme-spec.html#quasiquote
; https://github.com/exuanbo/cs61a-su19
(define-macro (def func bindings body)
    `(define ,(cons func bindings), body)
)
