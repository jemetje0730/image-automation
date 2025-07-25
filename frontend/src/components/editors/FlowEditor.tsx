import ReactFlow, {
  Background,
  Controls,
  MiniMap,
} from 'reactflow';
import 'reactflow/dist/style.css';

const initialNodes = [
  {
    id: '1',
    type: 'default',
    position: { x: 100, y: 100 },
    data: { label: 'Node 1' },
  },
];

const initialEdges = [];

export default function FlowEditor() {
  return (
    <div style={{ height: '100vh' }}>
      <ReactFlow nodes={initialNodes} edges={initialEdges} fitView>
        <MiniMap />
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
}
