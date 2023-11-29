import React from "react";
import { connect } from "react-redux";
import { ageUpAsync, ageDownAsync } from "../redux/actions/counterActions";

const Counter = ({ age, loading, ageUpAsync, ageDownAsync }) => {
  return (
    <div>
      <h2>Age: {age}</h2>
      <button onClick={() => ageUpAsync(1000)}>Age Up Async</button>
      <button onClick={() => ageDownAsync(1000)}>Age Down Async</button>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    age: state.counter.age,
    loading: state.counter.loading,
  };
};

export default connect(mapStateToProps, { ageUpAsync, ageDownAsync })(Counter);
