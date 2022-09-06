;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (unique s)  
  (cond
   ((null? s) s)
   (else (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))
  )
)

(define (cons-all first rests)
  (map (lambda (x) (cons first x)) rests)
)

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  'YOUR-CODE-HERE
)

; Tail recursion

(define (replicate x n)
  (define (replicate-tail x n result)
    (if (= n 0) result
      (replicate-tail x (- n 1) (append result (list x)))
    )
  )
  (replicate-tail x n (list))
)

(define (accumulate combiner start n term)
  (if (= n 1) (combiner start (term n)) 
    (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (if (= n 0) start
    (accumulate-tail combiner (combiner start (term n)) (- n 1) term)
  )
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)