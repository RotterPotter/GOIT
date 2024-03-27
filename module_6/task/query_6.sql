select st.name
from students st
join groups gr 
on st.id=gr.student_id
where gr.number_of_group=1; --put here number of group