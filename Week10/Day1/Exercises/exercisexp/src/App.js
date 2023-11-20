import ErrorBoundary from "./ErrorBoundary";
import Color from "./components/Color";
import Counter from "./components/Counter";
import Parent from "./components/Parent";

function App() {
  return (
    <div>
      {/* Exercise 1 */}

      {/* <h2>Simulation 1:</h2>
      <ErrorBoundary>
        <Counter />
        <Counter />
      </ErrorBoundary>

      <h2>Simulation 2:</h2>
      <ErrorBoundary>
        <Counter />
      </ErrorBoundary>
      <ErrorBoundary>
        <Counter />
      </ErrorBoundary>

      <h2>Simulation 3:</h2>
      <Counter /> */}

      {/* Exercise 2 */}
      {/* <Color /> */}

      {/* Exercise 3 */}
      <Parent />
    </div>
  );
}

export default App;
