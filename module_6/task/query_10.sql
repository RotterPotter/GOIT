select su.name as courses
from scores sc 
join subjects su on sc.subject_id=su.id
join students st on sc.student_id=st.id
join teachers t on su.teachers_id=t.id
where st.name='Christine Mills'
and t.name='Sandra Vega';
-- think that`s enough, thank you for reading