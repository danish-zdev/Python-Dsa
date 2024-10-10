function isValidType(propType, value) {
    const realType = typeof value;
    const types = ["string", "number", "bool", "int", "float"];
    return !types.includes(propType) || // handle 'any' type
      (propType === "string" && realType === "string") ||
      (propType === "number" && realType === "number") ||
      (propType === "bool" && realType === "boolean") ||
      (propType === "int" && realType === "number" && value % 1 === 0) ||
      (propType === "float" && realType === "number" && value % 1 !== 0);
  }
  
  function typeCheck(obj) {
    const target = Object.create(Object.getPrototypeOf(obj));
    const proxy = new Proxy(target, {
      set(_, prop, val) {
        const type = prop.split("_").pop();
        if(!isValidType(type, val)) {
          throw new Error(`Property ${prop} is not of type ${type}`);
        }
        return Reflect.set(...arguments);
      }
    });
    // Populate the proxy object with properties, which will throw if the object was initialized with invalid types
    Object.assign(proxy, obj);
    return proxy;
  }
  
  const obj = { age_int: 2, name_string: "Adam", job: null,};
  const validatingObject = typeCheck(obj);
  validatingObject.age_int = 2.25; // Throws error
  validatingObject.age_int = 2;
  validatingObject.job = "fireman";
  validatingObject.address_string = 20; // Throws error
  
  const obj_2 = {employed_bool: "true",};
  const validatingObject2 = typeCheck(obj_2); // Throws error