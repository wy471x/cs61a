(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))



;; Problem 17
;; Returns a list of two-element lists

(define (enumerate-helper s i)
  (if (null? (cdr s)) (cons (cons i (cons (car s) nil)) nil)
      (cons (cons i (cons (car s) nil)) (enumerate-helper (cdr s) (+ i 1)))
  )
)

(define (enumerate s)
  ; BEGIN PROBLEM 17
  (if (null? s) s
      (enumerate-helper s 0)
  )
)
  ; END PROBLEM 17

;; Problem 18

(define (zip-helper first_lst second_lst pairs)
  (if (null? (cdr pairs)) (cons ((car first_lst) (cons (car (car pairs)) nil))  (cons (car second_lst) (cons (car (cdr (car pairs))) nil)))
    (zip-helper (cons (car first_lst) (cons (car (car pairs)) nil)) (cons (car second_lst) (cons (car (cdr (car pairs))) nil)) (cdr pairs))
  )
)

(define (zip pairs)
  ; BEGIN PROBLEM 18
  (if (null? pairs) (cons pairs (cons pairs nil))
      (zip-helper (cons (car (car pairs)) nil) (cons (car (cdr (car pairs))) nil) (cdr pairs))
  )
)
  ; END PROBLEM 18


;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )))
