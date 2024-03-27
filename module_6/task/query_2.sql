select sc.student_id, st.name, su.name as subject_name, avg(sc.score) as avg_score
from students st
inner join scores sc on st.id=sc.student_id
inner join subjects su on sc.subject_id=su.id
where su.name='chemistry' -- type your subject here
group by sc.student_id, st.name, su.name
order by avg_score desc
limit 1;
