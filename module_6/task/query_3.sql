select gr.number_of_group, su.name, avg(sc.score) as avg_score
from scores sc
inner join subjects su on su.id=sc.subject_id 
inner join groups gr on sc.student_id=gr.student_id
where su.name='chemistry' -- put your subject here
group by gr.number_of_group, su.name
order by gr.number_of_group;