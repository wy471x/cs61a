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
  'YOUR-CODE-HERE
  )

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)