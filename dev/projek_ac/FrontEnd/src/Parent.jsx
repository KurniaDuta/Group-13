import axios from 'axios'
import { useState, useEffect } from 'react'
import Box from './Box'

export default function Parent() {
    const [update, setUpdate] = useState(0)
    const [watch, setWatch] = useState({
        jam: 0,
        menit: 0,
        detik: 0
    })

    useEffect(() => {
        getInfo()
        tm()
        const loop = setInterval(() => {
            setUpdate(e => (e == 0 ? 1 : 0))
        }, 1000)
        return () => clearInterval(loop)
    }, [update])


    const tm = () => {
        const wtc = new Date()
        let jam = wtc.getHours().toString()
        let menit = wtc.getMinutes().toString()
        let detik = wtc.getSeconds().toString()
        jam.length == 1 ? jam = 0 + jam : jam
        menit.length == 1 ? menit = 0 + menit : menit
        detik.length == 1 ? detik = 0 + detik : detik
        setWatch({
            jam: jam,
            menit: menit,
            detik: detik
        })
    }

    const getInfo = async () => {
        const values = await axios.get('http://192.168.58.209:5000/info')
        color(values.data)
    }

    const color = (info) => {
        const box1 = document.getElementsByClassName('text-lvl')[0]
        const box2 = document.getElementsByClassName('text-lvl')[1]
        const box3 = document.getElementsByClassName('text-lvl')[2]
        const box4 = document.getElementsByClassName('text-lvl')[3]

        info.fifth == 'h' ? box1.style.color = "rgb(155, 255, 139)" : box1.style.color = "rgb(255, 146, 139)"
        info.sixth == 'h' ? box2.style.color = "rgb(155, 255, 139)" : box2.style.color = "rgb(255, 146, 139)"
        info.seventh == 'h' ? box3.style.color = "rgb(155, 255, 139)" : box3.style.color = "rgb(255, 146, 139)"
        info.eighth == 'h' ? box4.style.color = "rgb(155, 255, 139)" : box4.style.color = "rgb(255, 146, 139)"
    }

    return (
        <>
            <div className="container-one">
                <div className='container-watch'>
                    <p className='text-watch'>{watch.jam} : {watch.menit} : {watch.detik}</p>
                </div>
            </div>
            <div className="container-two">
                <Box floor={"5"} path={"/fifth"} />
                <Box floor={"6"} path={"/sixth"} />
                <Box floor={"7"} path={"/seventh"} />
                <Box floor={"8"} path={"/eighth"} />
            </div>
        </>
    )
}