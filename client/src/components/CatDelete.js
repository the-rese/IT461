import { useLocation, useNavigate } from "react-router-dom";

const CatDelete = ({ deleteHandler }) => {
    const location = useLocation();
    const cat = location.state.cat;
    const navigate = useNavigate();
    const declineHandler = (e) => {
        e.preventDefault();
        navigate('/cats');
    }
    const confirmHandler = (e) => {
        e.preventDefault();
        deleteHandler(cat);
        navigate('/cats');
    }
    return (
        <>
            <div>Are you sure you want to delete this?</div>
            <form onSubmit={confirmHandler}>
                <button>Yes</button>
            </form>
            <form onSubmit={declineHandler}>
                <button>No</button>
            </form>
        </>
    );
}

export default CatDelete;