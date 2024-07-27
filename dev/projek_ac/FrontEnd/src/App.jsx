import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Parent from "./Parent"
import FifthFloor from "./FifthFloor"
import SixthFloor from "./SixthFloor"
import SeventhFloor from "./SeventhFloor"
import EighthFloor from "./EighthFloor"

export default function App() {
  return (
    <Router>
      <Routes>
        <Route
          exact
          path="/"
          element={<Parent />} />
        <Route
          path="/fifth"
          element={<FifthFloor />} />
        <Route
          path="/sixth"
          element={<SixthFloor />} />
        <Route
          path="/seventh"
          element={<SeventhFloor />} />
        <Route
          path="/eighth"
          element={<EighthFloor />} />
      </Routes>
    </Router>
  )
}
