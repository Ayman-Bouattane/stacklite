import React from 'react';
import { PieChart, Pie, Tooltip, ResponsiveContainer } from 'recharts';

export default function AvgQuestionLength({ avg }) {
  const data = [
    { name: 'Avg Length', value: avg },
    { name: 'Remaining', value: Math.max(0, 200 - avg) }
  ];

  return (
    <div className="mb-8">
      <h2 className="text-xl mb-2">Average Question Length</h2>
      <ResponsiveContainer width={300} height={300}>
        <PieChart>
          <Pie data={data} dataKey="value" nameKey="name" innerRadius={60} outerRadius={80} />
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}