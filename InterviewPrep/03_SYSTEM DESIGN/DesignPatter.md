Here are the **most important Object-Oriented Design (OOD) concepts** that are commonly asked and used in system design interviews (like Parking Lot, Elevator System, ATM, etc.):

---

### 🔑 **Core OOD Concepts**

1. **Abstraction**

   * Hides complex implementation details.
   * Focuses on *what* an object does, not *how* it does it.

2. **Encapsulation**

   * Bundles data and methods together.
   * Restricts direct access to internal state (use getters/setters).

3. **Inheritance**

   * Enables code reuse.
   * Allows child classes to inherit from parent (e.g., `Car` → `Vehicle`).

4. **Polymorphism**

   * Same interface, different behavior.
   * Example: `park()` behaves differently for `Bike` vs `Truck`.

---

### 📐 **SOLID Principles** (Very important in interviews)

1. **S** – Single Responsibility Principle
   A class should have only one reason to change.

2. **O** – Open/Closed Principle
   Open for extension, closed for modification.

3. **L** – Liskov Substitution Principle
   Subclasses should be replaceable for parent classes.

4. **I** – Interface Segregation Principle
   Prefer small, specific interfaces over large general ones.

5. **D** – Dependency Inversion Principle
   Depend on abstractions, not concrete implementations.

---

### 🧰 **Design Patterns** (Commonly used in LLD)

* **Singleton** – One global instance (e.g. ParkingLot, DB connection)
* **Strategy** – Replaceable algorithms (e.g. billing strategies)
* **Factory** – Object creation logic (e.g. create different Vehicle types)
* **Observer** – Notify components (e.g. sensor updates UI)

---

Would you like a cheat sheet PDF or quick flashcards on these for practice?

