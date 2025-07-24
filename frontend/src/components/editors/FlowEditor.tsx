import ReactFlow, { Background, Controls, MiniMap } from 'react-flow-renderer'

const initialNodes = []
const initialEdges = []

function FlowEditor() {
  return (
    <ReactFlow
      nodes={initialNodes}
      edges={initialEdges}
      fitView
    >
      <MiniMap />
      <Controls />
      <Background />
    </ReactFlow>
  )
}

export default FlowEditor
