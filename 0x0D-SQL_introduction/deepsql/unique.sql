-- after manipulate the databse
SELECT * FROM temp.temperatures LIMIT 10;





-- Count the number of distinct values in the university_city column
SELECT COUNT(DISTINCT(university_city))
FROM universities;


-- Update id with make + model
UPDATE cars
SET id = CONCAT(make, model);

-- Create the table
CREATE TABLE students (
  last_name VARCHAR(128) NOT NULL,
  ssn INT PRIMARY KEY,
  phone_no CHAR(12)
);


-- Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id;

-- Add a foreign key on professors referencing universities
ALTER TABLE professors
ADD CONSTRAINT professors_fkey FOREIGN KEY (university_id) REFERENCES universities (id);

-- Select all professors working for universities in the city of Zurich
SELECT professors.lastname, universities.id, universities.university_city
FROM professors
JOIN universities
ON professors.university_id = universities.id
WHERE universities.university_city = 'Zurich';


-- Add a professor_id column
ALTER TABLE affiliations
ADD COLUMN professor_id integer REFERENCES professors (id);

-- Rename the organization column to organization_id
ALTER TABLE affiliations
RENAME organization TO organization_id;

-- Add a foreign key on organization_id
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_fkey FOREIGN KEY (organization_id)
    REFERENCES organizations (id);


-- Populate the "professor_id" column
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname
     AND affiliations.lastname = professors.lastname;


-- Add a new foreign key constraint from affiliations to organizations which cascades deletion
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_id_fkey
     FOREIGN KEY (organization_id) REFERENCES organizations (id) ON DELETE CASCADE;

-- Filter the table and sort it
SELECT COUNT(*), organizations.organization_sector, 
professors.id, universities.university_city FROM affiliations
JOIN professors
     ON affiliations.professor_id = professors.id
JOIN organizations
     ON affiliations.organization_id = organizations.id
JOIN universities
     ON professors.university_id = universities.id
WHERE organizations.organization_sector = 'Media & communication'
GROUP BY 2,3,4
ORDER BY 1 DESC;