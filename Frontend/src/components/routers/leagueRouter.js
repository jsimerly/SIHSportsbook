import React from "react";
import {Navigate} from 'react-router-dom';


export default function LeagueRouter(props){
    console.log(props.user)
    console.log('here')
    
    if (props.currentLeague != '' && props.user.isLoggedIn == true) {
        return <Navigate to={'/sportsbook/' + props.currentLeague.league_id} />  
    }

    return <Navigate to='/new-league' /> 
}