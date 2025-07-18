---

# My Geospatial & Systems Programming Portfolio

Welcome to my portfolio! This repository showcases a selection of projects demonstrating my skills in **geospatial analysis, data management, and systems programming**. Each project highlights my approach to problem-solving, clean code architecture, and robust implementation.

---

## Featured Projects

### Book Records Manager (C)

This project is a robust **Book Records Manager** built in C, using a singly linked list to efficiently handle a collection of book records. It's a great example of core C programming principles in action.

**Key Highlights:**

* **Dynamic Memory Management:** Implemented proper memory allocation and deallocation to prevent leaks and optimize resource use.
* **Sorted Data Structures:** Utilized a singly linked list with sorted insertion by stock number for efficient data retrieval.
* **Modular Design:** Separated concerns into dedicated functions for data entry, list manipulation, and financial calculations, promoting code reusability and maintainability.
* **User-Friendly Interface:** Features a menu-driven interface for seamless interaction, allowing users to add, delete, view, and analyze records.
* **Error Handling:** Incorporated robust error handling for invalid input and potential memory failures, ensuring program stability.

This project demonstrates my proficiency in **pointer manipulation, manual memory control, and clean separation of concerns**, making it a solid example of low-level systems programming and data structure implementation.

### XML Tree Natural-Number Expression Evaluator (Java)

This Java project implements an **XML-based arithmetic expression evaluator** for natural numbers. It's designed with modularity in mind, leveraging existing components for parsing and computation.

**Key Highlights:**

* **Modular Architecture:** Leverages third-party libraries (`XMLTree1` for parsing, `NaturalNumber2` for arbitrary-precision arithmetic) to focus on core evaluation logic.
* **Recursive Evaluation:** The core `evaluate` method recursively traverses the XML tree, interpreting arithmetic operations (`<plus>`, `<minus>`, `<times>`, `<divide>`) and literal number nodes.
* **Arbitrary-Precision Arithmetic:** Utilizes `NaturalNumber2` for precise calculations, handling numbers of any size.
* **Defensive Programming:** Includes `divide-by-zero` checks and input validation through assertions, ensuring robust and reliable execution.
* **Separation of Concerns:** Clearly separates input/output handling from the core computation logic, promoting a clean and maintainable codebase.

This project highlights principles such as **reusable components, recursion, and maintainable, testable code structure**—key qualities in scalable software development.

### Bestaurants Geodatabase (PostgreSQL/PostGIS)

In this project, I designed and implemented a comprehensive **"Bestaurants" geospatial database** using PostgreSQL with PostGIS. It showcases my end-to-end proficiency in spatial database architecture.

**Key Highlights:**

* **Spatial Schema Design:** Applied a consistent spatial reference system (SRID 3857, WGS 84 Web Mercator) across all geometry-enabled tables.
* **Structured Data Storage:** Created `POINT`-based tables for various venue types (diners, cafés, restaurants, bars/lounges) with appropriate data types.
* **Data Integrity & Validation:** Implemented a `CHECK` constraint for ratings (1-5), an `ENUM` type for `venue_type`, and used foreign key constraints for a normalized one-to-many relationship between `diners` and `diner_reviews` to prevent orphaned records.
* **Efficient Spatial Queries:** Added **spatial indexes (GIST)** on geometry columns and **attribute indexes (BTREE)** on ratings to support high-performance spatial queries (e.g., finding diners with high ratings within a certain distance).
* **Reproducible Design:** Captured the complete schema in SQL scripts, ensuring version control, reproducibility, and automated deployment.

This project reinforced key principles of **relational modeling, spatial indexing, and data integrity**, while leveraging PostGIS capabilities to build scalable, high-performance geospatial applications.

---

## Geospatial Analysis & R Projects

### Transit Accessibility Study (R)

This project demonstrates a multimodal accessibility analysis of San Luis Obispo using R's modern transport-GIS stack.

**Key Highlights:**

* **Integrated R Libraries:** Utilized `r5r`, `osmextract`, `tidytransit`, `sf`, and the `tidyverse` for a complete analysis workflow.
* **Travel Time Matrix Generation:** Computed walk/transit travel times from schools to a city-wide hex grid using `travel_time_matrix()`.
* **Isochrone Generation:** Created and calculated areas for 10, 20, and 30-minute isochrones, visualizing accessibility.
* **Transit Network Analysis:** Processed GTFS data with `tidytransit` to count and visualize transit stops per grid cell.
* **Accessibility Modeling:** Applied `accessibility()` with both step and exponential decay functions to model and map spatial equity.

This project showcases reproducible, script-based approaches to **spatial network analysis, isochrones, and transit accessibility** using modern R tools.

### Spatial Network & Autocorrelation Analysis (R)

In this project, I conducted a full social and spatial network analysis of Seattle gang “turf” data entirely in R, integrating traditional spatial tools with modern network science packages.

**Key Highlights:**

* **Integrated R Ecosystem:** Combined `sf`, `tmap`, `spdep` with `igraph`, `tidygraph`, `ggraph`, `sfnetworks`, and `visNetwork` for a comprehensive analysis.
* **Data Preparation & Indexing:** Read and standardized census tract data to create composite indices like concentrated disadvantage.
* **Network Centrality Analysis:** Built a network from tract-level data, calculating and visualizing centrality metrics (degree, betweenness, closeness).
* **Spatial Autocorrelation:** Generated spatial weights and performed a Monte Carlo Moran’s I test to assess spatial clustering.
* **Geospatial Network Visualization:** Mapped centrality scores back to tracts and geometrically visualized the spatial network with `sfnetworks`.

This lab highlighted how R enables seamless integration of **spatial analysis, network science, and reproducible cartography** in one workflow.

### Wildfire Risk Assessment (R)

This capstone project, a group effort, utilized a modern RStudio-based GIS workflow to identify and analyze high-risk wildfire zones in Los Angeles County.

**Key Highlights:**

* **Multi-Source Data Integration:** Integrated 2022 fire-perimeter polygons, fire-station locations, and weekly drought-severity shapefiles.
* **Data Harmonization & Enrichment:** Harmonized projections, converted CSVs to spatial layers, and enriched wildfire polygons with alarm dates, area, and derived drought metrics.
* **Spatial Analysis & Proximity Modeling:** Quantified spatial intersections using `st_intersection` and `st_join`, and assessed proximity to fire stations via buffers and nearest-distance calculations.
* **Spatial Clustering & Point Pattern Analysis:** Used Moran’s I to test for spatial clustering of drought-driven fire risk and ran Ripley’s K for small fires to detect local clustering.
* **Reproducible GIS Workflow:** Demonstrated how emerging R-based GIS approaches enable integrated spatial analysis, proximity modeling, and high-quality mapping in a reproducible workflow.

---
