// Generated by gencpp from file carla_msgs/CarlaWeatherParameters.msg
// DO NOT EDIT!


#ifndef CARLA_MSGS_MESSAGE_CARLAWEATHERPARAMETERS_H
#define CARLA_MSGS_MESSAGE_CARLAWEATHERPARAMETERS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace carla_msgs
{
template <class ContainerAllocator>
struct CarlaWeatherParameters_
{
  typedef CarlaWeatherParameters_<ContainerAllocator> Type;

  CarlaWeatherParameters_()
    : cloudiness(0.0)
    , precipitation(0.0)
    , precipitation_deposits(0.0)
    , wind_intensity(0.0)
    , fog_density(0.0)
    , fog_distance(0.0)
    , wetness(0.0)
    , sun_azimuth_angle(0.0)
    , sun_altitude_angle(0.0)  {
    }
  CarlaWeatherParameters_(const ContainerAllocator& _alloc)
    : cloudiness(0.0)
    , precipitation(0.0)
    , precipitation_deposits(0.0)
    , wind_intensity(0.0)
    , fog_density(0.0)
    , fog_distance(0.0)
    , wetness(0.0)
    , sun_azimuth_angle(0.0)
    , sun_altitude_angle(0.0)  {
  (void)_alloc;
    }



   typedef float _cloudiness_type;
  _cloudiness_type cloudiness;

   typedef float _precipitation_type;
  _precipitation_type precipitation;

   typedef float _precipitation_deposits_type;
  _precipitation_deposits_type precipitation_deposits;

   typedef float _wind_intensity_type;
  _wind_intensity_type wind_intensity;

   typedef float _fog_density_type;
  _fog_density_type fog_density;

   typedef float _fog_distance_type;
  _fog_distance_type fog_distance;

   typedef float _wetness_type;
  _wetness_type wetness;

   typedef float _sun_azimuth_angle_type;
  _sun_azimuth_angle_type sun_azimuth_angle;

   typedef float _sun_altitude_angle_type;
  _sun_altitude_angle_type sun_altitude_angle;





  typedef boost::shared_ptr< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> const> ConstPtr;

}; // struct CarlaWeatherParameters_

typedef ::carla_msgs::CarlaWeatherParameters_<std::allocator<void> > CarlaWeatherParameters;

typedef boost::shared_ptr< ::carla_msgs::CarlaWeatherParameters > CarlaWeatherParametersPtr;
typedef boost::shared_ptr< ::carla_msgs::CarlaWeatherParameters const> CarlaWeatherParametersConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator1> & lhs, const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator2> & rhs)
{
  return lhs.cloudiness == rhs.cloudiness &&
    lhs.precipitation == rhs.precipitation &&
    lhs.precipitation_deposits == rhs.precipitation_deposits &&
    lhs.wind_intensity == rhs.wind_intensity &&
    lhs.fog_density == rhs.fog_density &&
    lhs.fog_distance == rhs.fog_distance &&
    lhs.wetness == rhs.wetness &&
    lhs.sun_azimuth_angle == rhs.sun_azimuth_angle &&
    lhs.sun_altitude_angle == rhs.sun_altitude_angle;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator1> & lhs, const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace carla_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bb273e4588ee8778c1dac74839d4709e";
  }

  static const char* value(const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbb273e4588ee8778ULL;
  static const uint64_t static_value2 = 0xc1dac74839d4709eULL;
};

template<class ContainerAllocator>
struct DataType< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
{
  static const char* value()
  {
    return "carla_msgs/CarlaWeatherParameters";
  }

  static const char* value(const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#\n"
"# Copyright (c) 2020 Intel Corporation.\n"
"#\n"
"# This work is licensed under the terms of the MIT license.\n"
"# For a copy, see <https://opensource.org/licenses/MIT>.\n"
"#\n"
"\n"
"float32 cloudiness\n"
"float32 precipitation\n"
"float32 precipitation_deposits\n"
"float32 wind_intensity\n"
"float32 fog_density\n"
"float32 fog_distance\n"
"float32 wetness\n"
"float32 sun_azimuth_angle\n"
"float32 sun_altitude_angle\n"
;
  }

  static const char* value(const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cloudiness);
      stream.next(m.precipitation);
      stream.next(m.precipitation_deposits);
      stream.next(m.wind_intensity);
      stream.next(m.fog_density);
      stream.next(m.fog_distance);
      stream.next(m.wetness);
      stream.next(m.sun_azimuth_angle);
      stream.next(m.sun_altitude_angle);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CarlaWeatherParameters_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::carla_msgs::CarlaWeatherParameters_<ContainerAllocator>& v)
  {
    s << indent << "cloudiness: ";
    Printer<float>::stream(s, indent + "  ", v.cloudiness);
    s << indent << "precipitation: ";
    Printer<float>::stream(s, indent + "  ", v.precipitation);
    s << indent << "precipitation_deposits: ";
    Printer<float>::stream(s, indent + "  ", v.precipitation_deposits);
    s << indent << "wind_intensity: ";
    Printer<float>::stream(s, indent + "  ", v.wind_intensity);
    s << indent << "fog_density: ";
    Printer<float>::stream(s, indent + "  ", v.fog_density);
    s << indent << "fog_distance: ";
    Printer<float>::stream(s, indent + "  ", v.fog_distance);
    s << indent << "wetness: ";
    Printer<float>::stream(s, indent + "  ", v.wetness);
    s << indent << "sun_azimuth_angle: ";
    Printer<float>::stream(s, indent + "  ", v.sun_azimuth_angle);
    s << indent << "sun_altitude_angle: ";
    Printer<float>::stream(s, indent + "  ", v.sun_altitude_angle);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CARLA_MSGS_MESSAGE_CARLAWEATHERPARAMETERS_H
