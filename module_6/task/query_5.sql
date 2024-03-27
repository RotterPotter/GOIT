select su.name as subjects
from subjects su
join teachers t on t.id=su.teachers_id
where t.name='Sandra Vega'; -- put here name of teacher
