import React from "react";
import {Navigate} from 'react-router-dom';


export default function LeagueRouter(props){
    console.log(props.user)
    console.log('here')

    if (props.user.isLoggedIn != null && props.user.isLoggedIn != false){
        let cLeague = props.currentLeague.league_id || props.leagues[0].league_id
        return <Navigate to={'/sportsbook/' + cLeague}/>
    }

    return <Navigate to='/login' /> 
}