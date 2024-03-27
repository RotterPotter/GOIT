select su.name as subjects
from scores sc
join subjects su on sc.subject_id=su.id
join students st on sc.student_id=st.id 
where st.name='Stephanie Baker'; -- ...