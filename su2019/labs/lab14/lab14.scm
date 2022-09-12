; Lab 14: Final Review

(define (compose-all funcs)
  (if (null? (cdr funcs)) (car funcs)
    ((car funcs) (compose-all (cdr funcs)))
  )
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond (_________________ ____________)
          (_________________ ____________)
          (else _________________________))
    )
  ______________________________
)

(define (contains? lst s)
  'YOUR-CODE-HERE
)