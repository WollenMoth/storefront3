import React from "react";

function Select({
  name,
  label,
  error,
  options,
  textProperty,
  valueProperty,
  ...rest
}) {
  return (
    <div className="mb-3">
      <label htmlFor={name} className="form-label">
        {label}
      </label>
      <select {...rest} name={name} id={name} className="form-control">
        <option value="" />
        {options.map((option) => (
          <option key={option[valueProperty]} value={option[valueProperty]}>
            {option[textProperty]}
          </option>
        ))}
      </select>
      {error && <div className="alert alert-danger">{error}</div>}
    </div>
  );
}

Select.defaultProps = {
  textProperty: "name",
  valueProperty: "id",
};

export default Select;
