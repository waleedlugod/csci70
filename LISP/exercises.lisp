; PART 1
; 1
(defun func (a b c)
    (- (+ a b) c)
)

; 2
(defun func (a)
    (* (- a 1) (- a 3))
)

; 3
(defun func (a)
    (if (= 2 (length a))
        (first a)
        (func (rest a))
    )
)

; 4
(defun func (a b)
    (if (= a 1)
        (first b)
        (func (- a 1) (rest b))
    )
)

; 8
(defun func (a)
    (if (= 3 (length a))
        (rest a)
        (func (rest a))
    )
)

; PART 2
(defun filterless (a x)
    (if (null x)
        nil
        (if (< (first x) a)
            (cons (first x) (filterless a (rest x)))
            (filterless a (rest x))
        )
    )
)
(defun filtermore (a x)
    (if (null x)
        nil
        (if (> (first x) a)
            (cons (first x) (filtermore a (rest x)))
            (filtermore a (rest x))
        )
    )
)
(defun qsort (L)
    (if (<= (length L) 1)
        L
        (append
            (qsort (filterless (first L) (rest L)))
            (append
                (list (first L))
                (qsort (filtermore (first L) (rest L)))
            )
        )
    )
)