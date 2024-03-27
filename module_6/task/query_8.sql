select t.name, su.name, avg(sc.score) as avg_score
from scores sc
join subjects su on sc.subject_id=su.id
join teachers t on t.id=su.teachers_id
where t.name='Heather Boyer' -- you already know
group by t.name, su.name; 