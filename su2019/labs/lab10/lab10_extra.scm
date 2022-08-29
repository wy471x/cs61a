;; Scheme ;;


(define lst 
  (cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))
)

(define (composed f g)
   (define (helper x)
      (f (g x))
    )
   helper
)

(define (remove item lst)
  (if (null? lst)
    (list)
    (if (eq? item (car lst))
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))
    )
  )

)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)


(define (no-repeats s)
 (cond 
  ((null? s) s)
  (else (cons (car s) (no-repeats (filter-lst (lambda (x) (not (= x (car s)))) (cdr s)))))
 )
)

(define (substitute s old new)
  (if (null? s)
    (list)
    (if (pair? (car s))
      (cons (substitute (car s) old new) (substitute (cdr s) old new))
      (if (equal? (car s) old)
        (cons new (substitute (cdr s) old new))
        (cons (car s) (substitute (cdr s) old new))
      )
    )
  )
)


(define (sub-all s olds news)
  (cond 
    ((and (null? olds) (null? news)) s)
    (else (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
  )
)