
import { useEffect, useRef } from "react";

const ITEM_DISTANCE = 80;
const SHIFT_DISTANCE = 400;
const CONTAINER_ORIGIN = -20;
const EASING = 0.05;

const PhotoQueue = (props:{imageData:string[]}) => {
  
  const el = useRef<HTMLDivElement>(null);
  let nextMouseShift = 0, nextZ = CONTAINER_ORIGIN;
  let currentMouseShift = 0, currentZ = CONTAINER_ORIGIN;
  const animId = useRef<number>(0);

  useEffect(() => {

    // Setup initial items angle
    const items = el.current!.children;

    for (let i = 0; i < items.length; i++) {
      const item = items[i] as HTMLDivElement;
      item.style.transform = `translateZ(${-i * ITEM_DISTANCE}px) translateX(0)`;
      item.dataset.index = i.toString();
    }

    // Move view based on mouse position
    const mouseHandler = (e:MouseEvent) => {
      nextMouseShift = (e.clientY / innerHeight - 0.5) * 10 - 20;
    }
    document.body.addEventListener('mousemove', mouseHandler);

    // Update container with easing parameters
    cancelAnimationFrame(animId.current);
    const updateFrame = () => {

      animId.current = requestAnimationFrame(updateFrame);
      currentMouseShift += (nextMouseShift - currentMouseShift) * EASING;
      currentZ += (nextZ - currentZ) * EASING;
      el.current!.style.transform = `rotateX(${currentMouseShift}deg) translateZ(${currentZ}px)`;
    }
    updateFrame();

  }, [props.imageData]);

  // Target an item, bring it to front
  function target(index:number) {

    const items = el.current!.children;
    const selectedItem = items[index] as HTMLDivElement;
    if (selectedItem.style.transform.indexOf('translateX(0px)') >= 0) index++;

    if (index >= items.length) return;
    nextZ = CONTAINER_ORIGIN + index * ITEM_DISTANCE;

    // Shift item
    for (let i = 0; i < items.length; i++) {

      const item = items[i] as HTMLDivElement;

      // Shift front items
      if (i < index)
        item.style.transform = `translateZ(${-i * ITEM_DISTANCE}px) translateX(${SHIFT_DISTANCE}px)`;
      // Shift back items
      else
        item.style.transform = `translateZ(${-i * ITEM_DISTANCE}px) translateX(0)`;
    }

  }
  return (
    <div className="container my-4">
      <div className="photoqueue" ref={el}>
        {props.imageData.map((it, index) => 
          <div 
              onClick={() => target(index)}
              key={index} 
              style={{backgroundImage:`url(${it})`}}
              className='photoqueue-item'>
          </div>)
        }
      </div>
    </div>
  )
}

export default PhotoQueue;
