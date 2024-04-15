import Image from 'next/image'
import React from 'react'
import Button from './Button'

export default function Hero() {
  return (
    <section className='max-container padding-container flex flex-col gap-20 py-10 pb-32 md:gap-28 lg:py-20 xl:flex-row border-2'>
        < div className='hero-map' />
        <div className=" relative z-20 flex flex-col xl:w-1/2" >
          < Image 
          src='/camp.svg'

          alt='camp'
          width={50}
          height={50}
          className=' absolute left-[-50px] top-[-30px] w-10 lg:w-[50px]'
          />
          <h1 className=' bold-52 lg:bold-88'>Hello my Hero</h1>
          <p className=' regular-16 mt-6 text-gray-30 xl:max-w-[520px]'>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Totam voluptates, et animi unde dolores sit blanditiis reprehenderit rem accusantium mollitia deleniti magni impedit magnam quibusdam aperiam numquam, consequatur dignissimos nobis.</p>
          <div className='my-11 flex flex-wrap gap-5'>
            <div className='flex items-center gap-2'>
                {Array(5).fill(1).map((_, index)=>(
                  <Image 
                  src='/star.svg'
                  key={index}
                  alt='star'
                  width={24}
                  height={24}
                  />
                ))}
            </div>
            <p className=' bold-16 lg:bold-20 text-blue-70'>124k</p>
            <span className='regular-16 lg:regular-20 ml-2'>hello my frend</span>
          </div>
          <div className='flex flex-col w-full gap-3 sm:flex-row'>
            <Button type="button"
             title='Dawnload App'
             variant='btn_green'
            /> 
            <Button type="button"
             title='Dawnload App?'
             icon='/play.svg'
             variant='btn_white_text'
            /> 
          </div>

        </div>

        <div className='relative flex flex-1 items-start'>
          <div className=' relative flex z-20 w-[238px] flex-col gap-13 rounded-3xl bg-green-90 px-6 py-8'>

            <div className=' flex flex-col'>
                <div className='flexBetween'>
                  <p className='regular-16 text-gray-20'>Locattion</p>
                  <Image
                  src='/close.svg'
                  alt='sjsjs'
                  width={24}
                  height={24}
                  />
                </div>
                <p className='text-white bold-20'>Agust calintes</p>
              </div>

              <div className='flexBetween'>
                  <div className=' flex flex-col'>
                    <p className=' regular-26 block text-gray-20'>Distance</p>
                    <p className=' text-white bold-20'>173.28 mi</p>
                  </div>
                  <div className=' flex flex-col'>
                    <p className=' regular-26 block text-gray-20'>Elevation</p>
                    <p className=' text-white bold-20'>173.28 km</p>
                  </div>
              </div>
          </div>
        </div>

    </section>
  )
}
