Systematic System Design!


What are your Requirements of the system?

What are Actors of the System?

Write out APIs signatures where the requirements are done by the Actors

Then Draw out your system. Don't just start drawing load balancers and caches without saying why you are going to use them. 


Unclear

I guess I should use a queue here, for publisher and subscriber?

---

I’ll partition by the foo_id or the bar_id

---

I could use a cache here.

---

An index will make it faster.

Reasonable

I will use a queue here to help decouple these services and make this component asynchronous from the rest. Whenever request to update a Foo comes in, the FooService publishes a message for the BarService to consume for processing.

---

I could partition by foo_id which would be good for X and Y but not good for Z. I could partition by bar_id which would be good for Y and Z but not good for W. 

Based on our requirements, this critical feature F receives most of the traffic so I’ll partition by the foo_id since it would help speed up that feature the most.

---

I could use a key-value cache that maps foo_id to bar_id so the getBar(foo_id) API can quickly get frequently accessed Bar resources. The cache entry would have to be invalidated when foo_id gets deleted.

---

An index on foo_points would improve read performance on the highest score but incurs more write latency which is acceptable for this read-heavy scenario.


For the logging system that multiple engineering teams are going to use

SQL

I could use a relational database to combine information across multiple tables. It doesn’t work well if the products have lots of different traits though because the schema has to be flexible (for example, cookies have calories and grams of sugar while sweaters have size and arm length).

vs. 
NoSQL

I could use a NoSQL database to handle the schema-less product traits but theres limited joining. This data in multiple tables don’t have to be joined a lot though so this limitation shouldn’t be a problem.

Reasonable

I will use SQL because the schema is static among all of the records.

I will use SQL because it's a read-heavy system with many relationships.

---

I will use document store because everyone’s dating profiles will have different preferences and interests set and sometimes not at all so I need a flexible schema.

I will use a document store because this is a write-intensive system that doesn’t involve a lot of relationships.
