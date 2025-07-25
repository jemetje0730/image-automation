import { ReactFlowProvider } from "reactflow";
import FlowEditor from "../components/editors/FlowEditor";

const Home = () => {
    return (
        <div className ="h-screen w-screen"> {/* Tailwind CSS */}
            <ReactFlowProvider>
                <FlowEditor />
            </ReactFlowProvider>

        </div>
    )
}

export default Home