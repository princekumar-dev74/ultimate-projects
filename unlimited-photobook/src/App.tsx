import { useState } from 'react'
import SearchInput from "./SearchInput"
import Photobook from "./Photobook"

function App() {

  const [data, setData] = useState<{imageData:string[]}>({imageData:[]})

  const setImageData = (data:string[]) => {
    setData({imageData:data})
  }

  return (
    <div className="w-screen h-screen p-2 flex flex-col items-center overflow-hidden">
      <h1 className='text-center font-bold text-2xl m-2'>React Photo Book</h1>
      <SearchInput setImageData={setImageData}/>
      <Photobook imageData={data.imageData}></Photobook>
    </div>
  )
}

export default App
