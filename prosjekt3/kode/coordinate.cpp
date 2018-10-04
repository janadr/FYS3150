#include <iostream>

#include "coordinate.hpp"

using namespace std;

Coordinate operator+ (const Coordinate &lhs, const Coordinate &rhs){
  Coordinate temp;
  temp.m_x = lhs.m_x + rhs.m_x;
  temp.m_y = lhs.m_y + rhs.m_y;
  temp.m_z = lhs.m_z + rhs.m_z;
  return temp;
}

Coordinate operator- (const Coordinate &lhs, const Coordinate &rhs){
  Coordinate temp;
  temp.m_x = lhs.m_x - rhs.m_x;
  temp.m_y = lhs.m_y - rhs.m_y;
  temp.m_z = lhs.m_z - rhs.m_z;
  return temp;
}

Coordinate operator* (double scalar, const Coordinate &rhs){
  Coordinate temp;
  temp.m_x = scalar * rhs.m_x;
  temp.m_y = scalar * rhs.m_y;
  temp.m_z = scalar * rhs.m_z;
  return temp;
}

Coordinate operator* (const Coordinate &lhs, double scalar){
  Coordinate temp;
  temp.m_x = lhs.m_x * scalar;
  temp.m_y = lhs.m_y * scalar;
  temp.m_z = lhs.m_z * scalar;
  return temp;
}

Coordinate operator/ (const Coordinate& lhs, double scalar){
  Coordinate temp;
  temp.m_x = lhs.m_x / scalar;
  temp.m_y = lhs.m_y / scalar;
  temp.m_z = lhs.m_z / scalar;
  return temp;
}

ostream &operator << (ostream &out, const Coordinate &rhs){
  out << rhs.m_x << ' ';
  out << rhs.m_y << ' ';
  out << rhs.m_z << endl;
  return out;
}