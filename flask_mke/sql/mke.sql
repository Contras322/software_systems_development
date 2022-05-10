select id, x1, y1, x2, y2, x3, y3
from (
	select s.id, n1, x1, y1, n2, x2, y2 from (
		select e.id, e.n1, n.x as x1, n.y as y1
		from fem.elements e
		left join fem.nodes n on e.n1=n.n_id
	) s
	join (
		select e.id, e.n2, n.x as x2, n.y as y2
		from fem.elements e
		left join fem.nodes n on e.n2=n.n_id
	) k
	on s.id = k.id
) r
left join (
	select l.id, l.n3, m.x as x3, m.y as y3
	from fem.elements l
	left join fem.nodes m
	on l.n3=m.n_id
) d
using(id)
LIMIT 0, 200