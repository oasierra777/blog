import { connect } from "react-redux";
import FullWidthLayouts from "hocs/layouts/FullWidthLayouts";

function Home() {
    return (
        <FullWidthLayouts>
            home
        </FullWidthLayouts>
    )
}

const mapStateToProps = state => ({

})

export default connect(mapStateToProps, {

})(Home);