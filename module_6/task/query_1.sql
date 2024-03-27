select sc.student_id, st.name, avg(sc.score) as avg_score
from scores sc join students st on st.id=sc.student_id
group by sc.student_id, st.name
order by avg_score desc
limit 5;