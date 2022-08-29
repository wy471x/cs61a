;; Scheme ;;


(define (over-or-under x y)
  'YOUR-CODE-HERE
  (if (< x y) 
      -1
      (if (= x y)
          0
          1
        )
    )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


(define (add-to-end lst x)
   (if (null? lst)
      (list x)
      (if (null? (cdr lst))
         (cons (car lst) (cons x nil))
         (cons (car lst) (add-to-end (cdr lst) x))
        )
    )
)


(define (filter-lst f lst)
  (if (null? lst)
     (list)
     (if (f (car lst))
        (cons (car lst) (filter-lst f (cdr lst)))
        (filter-lst f (cdr lst))
      )
    )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder num)
  'YOUR-CODE-HERE
  (define (adder x)
    (+ x num)
    )
  adder
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13