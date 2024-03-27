select st.name, sc.score
from scores sc 
join students st on st.id=sc.student_id
join groups gr on sc.student_id=gr.student_id
join subjects su on sc.subject_id=su.id
where su.name='chemistry' -- put here your subject
and gr.number_of_group='2'; -- and here you can put number of the group