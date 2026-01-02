import { useState } from 'react'
import SearchInput from './SearchInput';
import PhotoQueue from './PhotoQueue';

function App() {

  const [data, setData] = useState<{imageData:string[]}>({imageData:[]})

  const setImageData = (data:string[]) => {
    setData({imageData:data})
  }

  return (
    <div className="w-screen h-screen p-2 flex flex-col items-center overflow-hidden">
      <h1 className='text-center font-bold text-2xl m-2'>React Photo Queue</h1>
      <SearchInput setImageData={setImageData}/>
      <PhotoQueue imageData={data.imageData}></PhotoQueue>
    </div>
  )
}

export default App
