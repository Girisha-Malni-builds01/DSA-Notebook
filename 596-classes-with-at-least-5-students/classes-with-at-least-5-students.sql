select class from Courses group by class HAVING count(class)>=5;
