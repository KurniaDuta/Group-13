import { Link } from "react-router-dom"
import { useState, useEffect } from "react"
import axios from "axios"

let ind = [-1, -1]

export default function SeventhFloor() {
    const [update, setUpdate] = useState(0)
    const [temporary, setTemporary] = useState(0)
    const structureData = {
        ruang: "0",
        servis: "0",
        hari: "0",
        suhu: "0",
        standar: "0",
        kode: "h",
        status: "on"
    }
    const [datas, setDatas] = useState(Array.from({ length: 16 }, () => ({ ...structureData })))

    useEffect(() => {
        first()
        getdatas()
        color(datas)
        const loop = setInterval(() => {
            setUpdate(e => (e == 0 ? 1 : 0))
        }, 1000)
        return () => clearInterval(loop)
    }, [update])

    const first = () => {
        if (temporary == 0) {
            ind[0] = -1
        }
        setTemporary(e => (e == 0 ? 1 : e))
    }

    const changeStatus = (newStatus) => {
        if (ind[0] != -1) {
            if (newStatus != datas[ind[0]].status && datas[ind[0]].kode != "m") {
                colorButton(newStatus)
                const temporary = [...datas]
                temporary[ind[0]] = { ...temporary[ind[0]], status: newStatus }
                postStatus(temporary)
            }
        }
    }

    const getdatas = async () => {
        const values = await axios.get('http://localhost:5000/floor7g')
        setDatas(values.data)
        color(values.data)
    }

    const postStatus = async (temporary) => {
        const data = await axios.post('http://localhost:5000/floor7p', temporary)
    }

    return (
        <>
            <div className="container">
                <h1 className="text-floor">Lantai Tujuh</h1>
            </div>
            <div className="container-two">
                <div className="container-two-one">
                    <div className="container-two-one-two">
                        <ContainerTwoOneTwoOne start={0} value={datas} />
                        <ContainerTwoOneTwoOne start={8} value={datas} />
                    </div>
                </div>
                <div className="container-two-two">
                    <div className="container-two-two-one">
                        <div className="container-two-two-one-one">
                            <p className="information"></p>
                        </div>
                        <div className="container-two-two-one-one">
                            <p className="information"></p>
                        </div>
                        <div className="container-two-two-one-two space-between">
                            <button className="btn green" onClick={() => changeStatus("on")}>ON</button>
                            <button className="btn red" onClick={() => changeStatus("off")} >OFF</button>
                        </div>
                        <div className="container-two-two-one-two">
                            <Link to="/">
                                <button className="btn absolute">HOME</button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

function ContainerTwoOneTwoOne({ start, value }) {
    return (
        <>
            <div className="container-two-one-two-one">
                <ContainerTwoOneTwoOneOne start={start} value={value} />
                <ContainerTwoOneTwoOneOne start={start + 4} value={value} />
            </div>
        </>
    )
}

function ContainerTwoOneTwoOneOne({ start, value }) {
    return (
        <>
            <div className="container-two-one-two-one-one">
                <Card i={start} value={value} />
                <Card i={start + 1} value={value} />
                <Card i={start + 2} value={value} />
                <Card i={start + 3} value={value} />
            </div>
        </>
    )
}

function Card({ i, value }) {
    const btn = (indeks, msg1, msg2, status, datas) => {
        if (indeks != ind[0]) {
            const info = document.getElementsByClassName('information')
            ind[1] = ind[0]
            ind[0] = indeks

            const elemen = document.getElementsByClassName('container-two-one-two-one-one-one-two')
            elemen[ind[0]].classList.remove('up')
            elemen[ind[0]].classList.add('down')
            if (ind[1] != -1) {
                elemen[ind[1]].classList.remove('down')
                elemen[ind[1]].classList.add('up')
            }
            // color(datas)
            colorButton(status)
            info[0].innerText = msg1
            info[1].innerText = msg2
        }

    }
    return (
        <>
            <div className="container-two-one-two-one-one-one">
                <div className="container-two-one-two-one-one-one-one">
                    <div>
                        <h1 className="text-temperature">{value[i].suhu}</h1>
                        <h1 className="text-temperature">{value[i].standar}</h1>
                    </div>
                </div>
                <div className="container-two-one-two-one-one-one-two up">
                    <div className="container-two-one-two-one-one-one-one">
                        <h1 className="text-info">{value[i].ruang}</h1>
                    </div>
                </div>
                <div className="container-two-one-two-one-one-one-three">
                    <button className="btn-card" onClick={() => btn(i, value[i].servis, value[i].hari, value[i].status, value)}>
                    </button>
                </div>
            </div>
        </>
    )
}

function color(datas) {
    const elemen = document.getElementsByClassName('container-two-one-two-one-one-one-two')
    Array.from(elemen).map((elemens, idx) => {
        if (datas[idx].kode == "m") {
            elemens.style.backgroundColor = "rgb(255, 146, 139)"
        } else if (datas[idx].kode == "k") {
            elemens.style.backgroundColor = "rgb(255, 250, 139)"
        } else if (datas[idx].kode == "h") {
            elemens.style.backgroundColor = "rgb(155, 255, 139)"
        } else {
            elemens.style.backgroundColor = "rgb(240, 238, 238)"
        }
    })
}

const colorButton = (status) => {
    const btn = document.getElementsByClassName('btn')
    if (status == "on") {
        btn[0].style.backgroundColor = "rgb(155, 255, 139)"
        btn[1].style.backgroundColor = "rgb(255, 255, 255)"
    } else {
        btn[0].style.backgroundColor = "rgb(255, 255, 255)"
        btn[1].style.backgroundColor = "rgb(255, 146, 139)"
    }
}