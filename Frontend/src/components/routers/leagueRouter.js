import React from "react";
import {Navigate} from 'react-router-dom';


export default function LeagueRouter(props){
    if (props.currentLeague != '') {
        return <Navigate to={'/sportsbook/' + props.currentLeague.league_id} />  
    }

    return <Navigate to='/new-league' /> 
}