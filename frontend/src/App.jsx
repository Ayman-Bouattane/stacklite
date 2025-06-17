import React, { useEffect, useState } from 'react';
import { fetchInsights, fetchPrediction } from './api';
import TopTags from './components/TopTags';
import AvgQuestionLength from './components/AvgQuestionLength';
import ActivityHeatmap from './components/ActivityHeatmap';
import PredictionChart from './components/PredictionChart';

export default function App() {
  const [insights, setInsights] = useState(null);
  const [preds, setPreds] = useState([]);

  useEffect(() => {
    fetchInsights().then(res => setInsights(res.data));
    fetchPrediction(7).then(res => setPreds(res.data));
  }, []);

  if (!insights) return <div>Loading...</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">StackLite Dashboard</h1>
      <TopTags data={insights.top_tags} />
      <AvgQuestionLength avg={insights.avg_length} />
      <ActivityHeatmap data={insights.monthly_activity} />
      <PredictionChart data={preds} />
    </div>
  );
}